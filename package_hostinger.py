import os
import zipfile

def package_project():
    source_dir = r"c:\Users\miriam.castro\.gemini\antigravity\scratch\iao-website"
    zip_name = "iao_website_hostinger.zip"
    zip_path = os.path.join(source_dir, zip_name)

    exclude_exts = {'.py', '.ps1', '.zip', '.md'}
    exclude_dirs = {'node_modules', '.git', '__pycache__'}

    print(f"Empaquetando sitio web en {zip_path}...")
    
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(source_dir):
            # Exclude unwanted directories
            dirs[:] = [d for d in dirs if d not in exclude_dirs]
            
            for file in files:
                ext = os.path.splitext(file)[1].lower()
                if ext in exclude_exts or file == zip_name:
                    continue
                
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, source_dir)
                zipf.write(file_path, arcname)
                
    print(f"¡Empaquetado exitoso! Archivo creado: {zip_name}")

if __name__ == "__main__":
    package_project()
