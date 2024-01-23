import cv2 as cv
import numpy as np
def region_growing(image,threshold,seed):
    visited=np.zeros_like(image,dtype=np.uint8)
    segmented_region=np.zeros_like(image,dtype=np.uint8)
    stack=[seed]
    while stack:
        current_pixel=stack.pop()
        x,y=current_pixel
        if(x > 0 and y > 0 and x < image.shape[0]-1 and y < image.shape[1]-1 and not visited[x, y]):
            segmented_region[x,y]=255
            visited[x,y]=1
            if np.abs(int(image[x, y]) - int(image[x-1,y-1])) < threshold:
                stack.append((x-1,y-1))
            if np.abs(int(image[x,y]) - int(image[x,y-1])) < threshold:
                stack.append((x,y-1))
            if np.abs(int(image[x, y]) - int(image[x+1,y-1])) < threshold:
                stack.append((x+1,y-1))
            if np.abs(int(image[x,y]) - int(image[x-1,y])) < threshold:
                stack.append((x-1,y))
            if np.abs(int(image[x,y])-int(image[x+1,y])) < threshold:
                stack.append((x + 1, y))
            if np.abs(int(image[x, y]) - int(image[x-1,y+1])) < threshold:
                stack.append((x-1,y+1))
            if np.abs(int(image[x,y]) - int(image[x,y+1])) < threshold:
                stack.append((x,y+1))
            if np.abs(int(image[x,y]) - int(image[x+1,y+1])) < threshold:
                stack.append((x,y+1))
    return segmented_region
def region_splitting(image, threshold):
    height, width = image.shape
    segmented_region = np.zeros_like(image, dtype=np.uint8)
    def split_region(x, y, w, h):
        nonlocal segmented_region
        region = image[y:y+h, x:x+w]
        if np.std(region) < threshold:
            mean_intensity = np.mean(region)
            segmented_region[y:y+h, x:x+w] = mean_intensity
        else:
            split_w = w // 2
            split_h = h // 2
            split_region(x, y, split_w, split_h)
            split_region(x + split_w, y, split_w, split_h)
            split_region(x, y + split_h, split_w, split_h)
            split_region(x + split_w, y + split_h, split_w, split_h)
    split_region(0, 0, width, height)
    return segmented_region
def region_merging(image, threshold):
    height, width = image.shape
    labels = np.zeros_like(image, dtype=np.int32)
    current_label = 1
    def merge_regions(x, y, current_label):
        nonlocal labels
        queue = [(x, y)]
        while queue:
            current_pixel = queue.pop(0)
            cx, cy = current_pixel
            if (0 <= cx < width and 0 <= cy < height and labels[cy, cx] == 0 and abs(int(image[cy, cx]) - int(image[y, x])) < threshold):
                labels[cy, cx] = current_label
                queue.append((cx - 1, cy))
                queue.append((cx + 1, cy))
                queue.append((cx, cy - 1))
                queue.append((cx, cy + 1))
    for y in range(height):
        for x in range(width):
            if labels[y, x] == 0:
                merge_regions(x, y, current_label)
                current_label += 1
    segmented = np.zeros_like(image, dtype=np.uint8)
    colors = np.random.randint(0, 256, size=(current_label), dtype=np.uint8)

    for label in range(1, current_label):
        segmented[labels == label] = colors[label]
    return segmented
path="./Assets/test_2.jpg"
threshold=10
image= cv.imread(path,0)
cv.imshow("Segmented Region",region_growing(image,threshold,(130,110)))
cv.imshow("Region Spliting",region_splitting(image, threshold))
cv.imshow("Region Merging",region_merging(image,threshold))
cv.imshow("Orginal",image)
cv.waitKey(0)