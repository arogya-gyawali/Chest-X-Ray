import os
import random
import shutil

# ---------------------------
# CONFIGURATION
# ---------------------------
source_dir = 'Clean_ChestXRay_Dataset'  # Folder with all images per class
target_dir = 'dataset_split'            # Folder to create train/test split
train_ratio = 0.8                        # Fraction of data for training
seed = 42                                # For reproducibility

random.seed(seed)

# ---------------------------
# CREATE MAIN FOLDERS
# ---------------------------
train_dir = os.path.join(target_dir, 'train')
test_dir = os.path.join(target_dir, 'test')
os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

# ---------------------------
# SPLIT DATASET
# ---------------------------
for class_name in os.listdir(source_dir):
    class_path = os.path.join(source_dir, class_name)
    if not os.path.isdir(class_path):
        continue

    # Create class subfolders
    os.makedirs(os.path.join(train_dir, class_name), exist_ok=True)
    os.makedirs(os.path.join(test_dir, class_name), exist_ok=True)

    # Get all images
    images = [f for f in os.listdir(class_path) if f.lower().endswith('.png')]
    random.shuffle(images)

    # Split into train/test
    split_idx = int(len(images) * train_ratio)
    train_images = images[:split_idx]
    test_images = images[split_idx:]

    # Copy images
    for img in train_images:
        shutil.copy(os.path.join(class_path, img), os.path.join(train_dir, class_name, img))
    for img in test_images:
        shutil.copy(os.path.join(class_path, img), os.path.join(test_dir, class_name, img))

    print(f"✅ {class_name}: {len(train_images)} train, {len(test_images)} test")

print("🎉 Dataset successfully split into training and test sets!")
