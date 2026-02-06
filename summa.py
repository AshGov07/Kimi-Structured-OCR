# import cv2

# # Load image
# img = cv2.imread(r"C:\Users\Welcome\Downloads\Sonocare Images\Sonocare Images\Samsung HS40\55 (2).jpg")

# # Convert to grayscale
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# # Apply Gaussian blur
# blur = cv2.GaussianBlur(gray, (5,5), 0)

# # Edge detection
# edges = cv2.Canny(blur, 50, 150)

# # Find contours
# contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# # Loop through contours
# for cnt in contours:
#     x, y, w, h = cv2.boundingRect(cnt)
    
#     # Filter by size (adjust thresholds depending on image)
#     if w > 100 and h > 50:  
#         cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

# # Show result
# cv2.imshow("Detected Boxes", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# import cv2
# import pytesseract

# # Point to where Tesseract is installed
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"


# # --- Step 1: Load image ---
# img = cv2.imread(r"C:\Users\Welcome\Downloads\Sonocare Images\Sonocare Images\Samsung HS40\55 (2).jpg")   # replace with your filename
# h, w = img.shape[:2]

# # --- Step 2: Crop right side (where table usually is) ---
# roi = img[0:h, int(w):w]   # keep right 100% of the image

# # --- Step 3: Preprocess ---
# gray = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
# # Adaptive thresholding handles uneven brightness
# thresh = cv2.adaptiveThreshold(gray, 255,
#                                cv2.ADAPTIVE_THRESH_MEAN_C,
#                                cv2.THRESH_BINARY_INV, 15, 10)

# # --- Step 4: Morphological operations ---
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
# morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# # --- Step 5: Find contours ---
# contours, _ = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# boxes = []
# for cnt in contours:
#     x,y,w,h = cv2.boundingRect(cnt)
#     aspect_ratio = w / float(h)
#     # Filter likely table/box regions
#     if 1.5 < aspect_ratio < 6 and w > 80 and h > 20:
#         boxes.append((x,y,w,h))
#         cv2.rectangle(roi, (x,y), (x+w,y+h), (0,255,0), 2)

# # --- Step 6: OCR on cropped ROI ---
# # You can OCR the whole ROI or each detected box separately
# text = pytesseract.image_to_string(roi)
# print("Extracted Text:\n", text)

# # --- Step 7: Show result ---
# cv2.imshow("Detected Table", roi)
# cv2.waitKey(0)
# cv2.destroyAllWindows()




# import cv2
# import pytesseract
# import re

# # Point to where Tesseract is installed
# pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# # --- Step 1: Load image ---
# img = cv2.imread(r"C:\Users\Welcome\Downloads\Sonocare Images\Sonocare Images\Samsung HS40\55 (2).jpg")
# if img is None:
#     raise ValueError("Image not found. Check the path!")

# h, w = img.shape[:2]

# # --- Step 2: Preprocess full image ---
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# thresh = cv2.adaptiveThreshold(gray, 255,
#                                cv2.ADAPTIVE_THRESH_MEAN_C,
#                                cv2.THRESH_BINARY_INV, 15, 10)

# # --- Step 3: Morphological operations ---
# kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5,5))
# morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# # --- Step 4: Find contours ---
# contours, _ = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# for cnt in contours:
#     x,y,w,h = cv2.boundingRect(cnt)
#     aspect_ratio = w / float(h)
#     # Filter likely table/box regions
#     if 1.5 < aspect_ratio < 6 and w > 80 and h > 20:
#         cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)

# # --- Step 5: OCR on full image ---
# text = pytesseract.image_to_string(img)
# print("Extracted Text:\n", text)

# # --- Step 6: Parse values with regex ---
# parsed = {}
# patterns = {
#     "GA": r"GA\s*([\d]+w[\d]+d)",
#     "FL": r"FL\s*([\d]+w[\d]+d)",
#     "EFW": r"EFW\s*([\d]+w[\d]+d)",
#     "Age": r"Age[: ]\s*(\d+)"
# }

# for key, pattern in patterns.items():
#     match = re.search(pattern, text)
#     if match:
#         parsed[key] = match.group(1)

# print("\nStructured Data Extracted:")
# for k,v in parsed.items():
#     print(f"{k}: {v}")

# # --- Step 7: Show result ---
# cv2.imshow("Detected Boxes", img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()



import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# --- Step 1: Load image ---
img = cv2.imread(r"C:\Users\Welcome\Downloads\Sonocare Images\Sonocare Images\Samsung HS40\55 (2).jpg")
if img is None:
    raise ValueError("Image not found. Check path!")

h, w = img.shape[:2]

# --- Step 2: Preprocess full image ---
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.adaptiveThreshold(gray, 255,
                               cv2.ADAPTIVE_THRESH_MEAN_C,
                               cv2.THRESH_BINARY_INV, 15, 10)

# --- Step 3: Morphological operations (larger kernel) ---
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15,15))
morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)

# --- Step 4: Find contours ---
contours, _ = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

for cnt in contours:
    x,y,wc,hc = cv2.boundingRect(cnt)
    area = cv2.contourArea(cnt)
    aspect_ratio = wc / float(hc)

    # Filter: large area + rectangular + near left/right margin
    if area > 5000 and 1.2 < aspect_ratio < 6 and (x < w*0.2 or x > w*0.7):
        cv2.rectangle(img, (x,y), (x+wc,y+hc), (0,255,0), 3)

# --- Step 5: OCR only on detected region ---
roi = img[y:y+hc, x:x+wc]
text = pytesseract.image_to_string(roi)
print("Extracted Text:\n", text)

# --- Step 6: Show result ---
cv2.imshow("Detected Table", img)
cv2.waitKey(0)
cv2.destroyAllWindows()