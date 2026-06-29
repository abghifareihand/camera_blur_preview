import cv2
import mediapipe as mp
import math

def get_distance(p1, p2):
    """Menghitung jarak Euclidean antara dua titik landmark."""
    return math.sqrt((p1.x - p2.x)**2 + (p1.y - p2.y)**2)

def main():
    # 1. Inisialisasi MediaPipe Hands
    mp_hands = mp.solutions.hands
    mp_draw = mp.solutions.drawing_utils

    hands = mp_hands.Hands(
        static_image_mode=False,
        max_num_hands=2,
        min_detection_confidence=0.7,
        min_tracking_confidence=0.7
    )

    # 2. Inisialisasi Kamera
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Kamera tidak dapat diakses!")
        return

    # Mode Deteksi Blur:
    # 0 = Mode 1 Tangan (2 Jari)
    # 1 = Mode 2 Tangan (2 Jari)
    # 2 = Mode 1 Tangan (Semua Jari Terbuka)
    blur_mode = 0

    print("=== APLIKASI CAMERA PREVIEW DENGAN 3 MODE BLUR ===")
    print("Petunjuk:")
    print("- Tekan tombol 'm' pada keyboard -> Mengganti Mode Deteksi.")
    print("- Tekan tombol 'q' pada keyboard -> Keluar.")
    print("--------------------------------------------------")
    print("Daftar Mode:")
    print("1. [Mode 0] 1 Tangan (2 Jari) -> Telunjuk & Tengah.")
    print("2. [Mode 1] 2 Tangan (2 Jari) -> Kedua tangan menunjukkan 2 jari.")
    print("3. [Mode 2] 1 Tangan (Semua Terbuka) -> Layar blur jika semua jari terbuka, normal jika mengepal.")
    print("==================================================")

    while True:
        success, frame = cap.read()
        if not success:
            print("Gagal membaca frame.")
            break

        # Efek mirror (balik horizontal)
        frame = cv2.flip(frame, 1)
        h, w, _ = frame.shape

        # Konversi warna ke RGB untuk MediaPipe
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(rgb_frame)

        should_blur = False
        hands_info = [] # Menyimpan info jari per tangan

        # Jika ada tangan terdeteksi
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                landmarks = hand_landmarks.landmark
                wrist = landmarks[0]

                # Cek 4 jari utama (Telunjuk, Tengah, Manis, Kelingking)
                tip_ids = [8, 12, 16, 20]
                pip_ids = [6, 10, 14, 18]

                fingers = []
                for tip, pip in zip(tip_ids, pip_ids):
                    # Cek Vertikal & Cek Jarak Pergelangan
                    vertical_open = landmarks[tip].y < landmarks[pip].y
                    dist_tip = get_distance(landmarks[tip], wrist)
                    dist_pip = get_distance(landmarks[pip], wrist)
                    distance_open = dist_tip > dist_pip

                    if vertical_open and distance_open:
                        fingers.append(1)
                    else:
                        fingers.append(0)

                total_fingers = sum(fingers)
                hands_info.append(total_fingers)

                # Gambar skeleton tangan di layar
                mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Logika Pemicu Blur berdasarkan Mode yang dipilih
            if blur_mode == 0:
                # Mode 0: 1 Tangan (2 Jari)
                if any(count == 2 for count in hands_info):
                    should_blur = True
            elif blur_mode == 1:
                # Mode 1: 2 Tangan (2 Jari)
                if len(hands_info) == 2 and all(count == 2 for count in hands_info):
                    should_blur = True
            elif blur_mode == 2:
                # Mode 2: 1 Tangan (Semua Jari Terbuka / 4 Jari terangkat)
                if any(count == 4 for count in hands_info):
                    should_blur = True

        # 3. Proses Blur jika kondisi pemicu terpenuhi
        if should_blur:
            frame = cv2.GaussianBlur(frame, (99, 99), 0)

        # 4. Gambar UI Overlay Premium
        # Header Latar Belakang Transparan
        cv2.rectangle(frame, (0, 0), (w, 75), (30, 30, 30), cv2.FILLED)

        # Teks nama mode yang sedang aktif
        mode_names = {
            0: "MODE: 1 TANGAN (2 JARI)",
            1: "MODE: 2 TANGAN (2 JARI)",
            2: "MODE: 1 TANGAN (SEMUA JARI TERBUKA)"
        }
        cv2.putText(frame, mode_names[blur_mode], (20, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 200, 0), 2)
        cv2.putText(frame, "[m] Ganti Mode | [q] Keluar", (20, 55), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (200, 200, 200), 1)

        # Menampilkan Status Sensor Blur
        if should_blur:
            cv2.rectangle(frame, (w - 180, 15), (w - 20, 55), (0, 0, 255), cv2.FILLED)
            cv2.putText(frame, "BLUR: ACTIVE", (w - 165, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)
        else:
            cv2.rectangle(frame, (w - 180, 15), (w - 20, 55), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, "BLUR: INACTIVE", (w - 170, 40), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

        # 5. Tampilkan Window Preview
        cv2.imshow("Camera Preview - Gesture Blur", frame)

        # 6. Kontrol Keyboard
        key = cv2.waitKey(1) & 0xFF
        if key == ord('q'):
            break
        elif key == ord('m'):
            # Berputar di antara mode 0, 1, dan 2
            blur_mode = (blur_mode + 1) % 3
            print(f"Mode diubah ke: {mode_names[blur_mode]}")

    cap.release()
    cv2.destroyAllWindows()
    print("Aplikasi ditutup.")

if __name__ == "__main__":
    main()
