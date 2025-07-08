import cv2
import numpy as np

def detect_tiny_blobs(frame, bg_subtractor=None, diff_thresh=25, max_size=3):
    """
    Detect connected‐component blobs up to max_size×max_size pixels
    contrasting with the background.
    
    Args:
      frame          – BGR image from camera
      bg_subtractor  – cv2.BackgroundSubtractor (optional)
      diff_thresh    – pixel‐difference threshold
      max_size       – maximum width/height in pixels for detected blobs
    
    Returns:
      mask            – binary mask of detected tiny blobs
      blob_bboxes     – list of (x, y, w, h) for each blob
    """
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # 1) Get a foreground mask
    if bg_subtractor is None:
        # Simple frame‐difference to a fixed “background” (first frame)
        raise ValueError("bg_subtractor required for dynamic scenes")
    fg_mask = bg_subtractor.apply(gray)
    
    # 2) Threshold to clean it up
    _, thresh = cv2.threshold(fg_mask, diff_thresh, 255, cv2.THRESH_BINARY)
    
    # 3) Optional: morphological opening to remove noise
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (2,2))
    clean = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
    
    # 4) Connected components
    num_labels, labels, stats, centroids = cv2.connectedComponentsWithStats(clean)
    # stats: [label, x, y, w, h, area]
    
    mask = np.zeros_like(clean)
    blob_bboxes = []
    for i in range(1, num_labels):
        x, y, w, h, area = stats[i]
        # Filter by max width & height
        if w <= max_size and h <= max_size and area >= 1:
            blob_bboxes.append((x, y, w, h))
            mask[labels == i] = 255
    
    return mask, blob_bboxes

def main():
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Cannot open camera")
        return

    # Optional: set higher resolution
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

    # Initialize a background subtractor (e.g. MOG2)
    backSub = cv2.createBackgroundSubtractorMOG2(
        history=100,
        varThreshold=16,
        detectShadows=False
    )
    
    while True:
        ret, frame = cap.read()
        if not ret:
            break
        
        # Detect tiny blobs
        mask, blobs = detect_tiny_blobs(
            frame,
            bg_subtractor=backSub,
            diff_thresh=25,
            max_size=3
        )
        
        # Count them!
        num_blobs = len(blobs)
        print(f"[INFO] Blobs detected in frame: {num_blobs}")
        
        # Overlay rectangles + blob count
        vis = frame.copy()
        for (x, y, w, h) in blobs:
            cv2.rectangle(vis, (x, y), (x + w - 1, y + h - 1), (0, 0, 255), 1)
        
        # Draw blob count as text
        cv2.putText(
            vis,
            f"Blob count: {num_blobs}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1.0,
            (0, 255, 0),
            2
        )
        
        # Show both mask and overlay
        cv2.imshow("Tiny-Blob Mask", mask)
        cv2.imshow("Detected Blobs", vis)
        
        if cv2.waitKey(1) & 0xFF == 27:  # ESC
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
