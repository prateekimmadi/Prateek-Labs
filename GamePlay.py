const int buttonPins[] = {16, 17, 18, 19};
const int ledPins[] = {0, 1, 3, 4};

void setup() {
  // Initialize LEDs as OUTPUT
  for (int i = 0; i < 4; i++) {
    pinMode(ledPins[i], OUTPUT);
  }

  // Initialize buttons as INPUT_PULLUP
  for (int i = 0; i < 4; i++) {
    pinMode(buttonPins[i], INPUT_PULLUP);
  }
}

void loop() {
  // Check the state of each button
  for (int i = 0; i < 4; i++) {
    if (digitalRead(buttonPins[i]) == LOW) { // Button is pressed
      digitalWrite(ledPins[i], HIGH);       // Turn on the corresponding LED
    } else {
      digitalWrite(ledPins[i], LOW);        // Turn off the corresponding LED
    }
  }
}
const int buttonPins[] = {16, 17, 18, 19}; // Button pins
const int ledPins[] = {0, 1, 2, 3};    // LED pins
const int numButtons = 4;              // Number of buttons
const int maxSequence = 10;            // Maximum sequence length

int sequence[maxSequence]; // Store the sequence of LEDs
int playerSequence[maxSequence]; // Store the player's input sequence

int sequenceLength = 0; // Current length of the sequence
int playerTurn = false; // Player's turn flag
int gameStarted = false; // Game started flag
int buttonState[numButtons]; // Store the state of each button
int lastButtonState[numButtons]; // Store the previous state of each button

void setup() {
  // Initialize LEDs as OUTPUT
  for (int i = 0; i < numButtons; i++) {
    pinMode(ledPins[i], OUTPUT);
  }

  // Initialize buttons as INPUT_PULLUP
  for (int i = 0; i < numButtons; i++) {
    pinMode(buttonPins[i], INPUT_PULLUP);
  }

  // Initialize random seed
  randomSeed(analogRead(0));
  
  // Start the game
  startGame();
}

void loop() {
  if (gameStarted) {
    if (!playerTurn) {
      // It's the computer's turn to add to the sequence
      addRandomToSequence();
      showSequence();
      playerTurn = true;
    } else {
      // It's the player's turn to repeat the sequence
      getPlayerInput();
    }
  }
}

void startGame() {
  sequenceLength = 0;
  playerTurn = false;
  gameStarted = true;
}

void addRandomToSequence() {
  sequence[sequenceLength] = random(0, numButtons);
  sequenceLength++;
}

void showSequence() {
  for (int i = 0; i < sequenceLength; i++) {
    digitalWrite(ledPins[sequence[i]], HIGH);
    delay(500);
    digitalWrite(ledPins[sequence[i]], LOW);
    delay(300);
  }
}

void getPlayerInput() {
  for (int i = 0; i < numButtons; i++) {
    buttonState[i] = digitalRead(buttonPins[i]);
    if (buttonState[i] == LOW && lastButtonState[i] == HIGH) {
      // Button is pressed
      digitalWrite(ledPins[i], HIGH);
      playerSequence[sequenceLength - 1] = i;
      delay(200);
      digitalWrite(ledPins[i], LOW);
    }
    lastButtonState[i] = buttonState[i];
  }

  if (sequenceLength > 0 && checkPlayerInput()) {
    // Player's input is correct so far
    if (sequenceLength == maxSequence) {
      // Player has completed the game
      gameStarted = false;
      // You can add some winning animation here
      delay(1000);
      startGame(); // Start a new game
    }
  } else {
    // Player made a mistake
    gameStarted = false;
    // You can add some losing animation here
    delay(1000);
    startGame(); // Start a new game
  }
}

bool checkPlayerInput() {
  for (int i = 0; i < sequenceLength; i++) {
    if (playerSequence[i] != sequence[i]) {
      return false;
    }
  }
  return true;
}

