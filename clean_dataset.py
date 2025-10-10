import os
import shutil

def clean_covid_dataset(root_dir='COVID-19_Radiography_Dataset', clean_dir='Clean_ChestXRay_Dataset'):
    """
    Cleans and organizes the COVID-19 Radiography dataset into a simpler format:
    
    Clean_ChestXRay_Dataset/
    ├── covid/
    ├── pneumonia/
    └── normal/
    """

    # Classes to include (map original folder names to new folder names)
    class_map = {
        'COVID': 'covid',
        'pneumonia': 'pneumonia',
        'normal': 'normal'
    }

    # Create the clean dataset folder
    os.makedirs(clean_dir, exist_ok=True)

    for orig_class, new_class in class_map.items():
        # Path to original images
        img_dir = os.path.join(root_dir, orig_class, 'images')
        if not os.path.isdir(img_dir):
            print(f"⚠️ Skipping {orig_class} — folder not found at {img_dir}")
            continue

        # Path to new clean class folder
        clean_class_dir = os.path.join(clean_dir, new_class)
        os.makedirs(clean_class_dir, exist_ok=True)

        # Copy all .png files from images/ to clean dataset
        images = [f for f in os.listdir(img_dir) if f.lower().endswith('.png')]
        for img in images:
            src = os.path.join(img_dir, img)
            dst = os.path.join(clean_class_dir, img)
            shutil.copy(src, dst)

        print(f"✅ Copied {len(images)} images to {clean_class_dir}")

    print("\n🎉 Clean dataset created successfully!")


if __name__ == "__main__":
    # Run the cleaning process
    clean_covid_dataset()
