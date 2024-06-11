import cv2
import mediapipe as mp
import time

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands()

cap = cv2.VideoCapture(0)  # Use 0 instead of 1, unless your webcam is on index 1

while cap.isOpened():
    success, img = cap.read()
    if not success:
        print("Ignoring empty camera frame.")
        continue

    # Convert the image to RGB
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    # Process the image with MediaPipe Hands
    results = hands.process(img_rgb)

    # Draw hand landmarks if detected
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            for lm in hand_landmarks.landmark:
                # Draw landmarks on the image (you can customize this part)
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

    # Display the image
    cv2.imshow("Hand Tracking", img)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Clean up
cap.release()
cv2.destroyAllWindows()
