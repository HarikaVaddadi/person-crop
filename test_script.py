import torch
from utils.general import xyxy2xywh
# Given parameters
xyxy = [100, 150, 300, 400]  # [x1, y1, x2, y2]
gain = 1.02
horizontal_pad_percent = 1.0  # 10% of width
vertical_pad_percent = 0.5    # 25% of height

# Convert to tensor and calculate xywh boxes
xyxy = torch.tensor(xyxy).view(-1, 4)
b = xyxy2xywh(xyxy)
print(b)
# Calculate padded dimensions
b[:, 2] = b[:, 2] * gain + b[:, 2] * horizontal_pad_percent  # box w * gain + horizontal_pad
b[:, 3] = b[:, 3] * gain + b[:, 3] * vertical_pad_percent    # box h * gain + vertical_pad

print("Padded Bounding Box Dimensions (xywh):")
print(b)


c = b[:, 2] * gain + b[:, 2]
d = b[:, 3] * gain + b[:, 3]

print(c,d, b[:, 2] )
