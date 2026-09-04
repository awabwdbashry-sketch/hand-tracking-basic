import cv2
import mediapipe as mp

# إعداد MediaPipe Hands
mp_hands = mp.solutions.hands

hands = mp_hands.Hands(
    static_image_mode=False,
    max_num_hands=2,              # تتبع يدين
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

# أدوات الرسم
mp_draw = mp.solutions.drawing_utils

# تشغيل الكاميرا
cap = cv2.VideoCapture(0)

while True:

    success, frame = cap.read()

    if not success:
        break

    # قلب الصورة (Mirror)
    frame = cv2.flip(frame, 1)

    # تحويل BGR إلى RGB
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # تحليل الصورة
    results = hands.process(rgb)

    # إذا تم اكتشاف يد أو أكثر
    if results.multi_hand_landmarks:

        for hand_landmarks in results.multi_hand_landmarks:

            # رسم اليد
            mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                mp_hands.HAND_CONNECTIONS,
                mp_draw.DrawingSpec(
                    color=(0, 255, 0),
                    thickness=2,
                    circle_radius=3
                ),
                mp_draw.DrawingSpec(
                    color=(255, 0, 255),
                    thickness=2
                )
            )

    # عرض الكاميرا
    cv2.imshow("Hand Tracking", frame)

    # الخروج عند الضغط على q
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# تنظيف الموارد
cap.release()
cv2.destroyAllWindows()