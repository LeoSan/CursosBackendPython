import os
import json
import re

def clean_title(filename):
    # Remover la extensión .pdf
    name_without_ext = filename.replace('.pdf', '')
    # Reemplazar guiones bajos o medios por espacios
    name_cleaned = re.sub(r'[-_]', ' ', name_without_ext)
    # Capitalizar apropiadamente si se desea, o simplemente dejarlo así
    return name_cleaned

def extract_pdfs(root_dir):
    pdf_list = []
    
    # Carpetas a ignorar
    ignore_dirs = {'.git', 'node_modules', '.vscode', 'venv', 'env', '__pycache__'}
    
    for dirpath, dirnames, filenames in os.walk(root_dir):
        # Modificamos dirnames in-place para que os.walk ignore esas carpetas
        dirnames[:] = [d for d in dirnames if d not in ignore_dirs]
        
        for file in filenames:
            if file.lower().endswith('.pdf'):
                # Ruta absoluta al archivo
                full_path = os.path.join(dirpath, file)
                
                # Ruta relativa desde la raíz del proyecto
                rel_path = os.path.relpath(full_path, root_dir)
                
                # Para asegurar la misma compatibilidad en web (siempres usar /)
                rel_path_web = rel_path.replace('\\', '/')
                
                title = clean_title(file)
                
                pdf_obj = {
                    "anio": "",
                    "url": f"/{rel_path_web}",
                    "titulo": title,
                    "texto": title,
                    "enlace": "",
                    "empresa": ""
                }
                pdf_list.append(pdf_obj)
                
    return pdf_list

def main():
    # Asume que el script se ejecuta desde la raíz o scripts/ 
    # y queremos inspeccionar la raíz del proyecto
    script_dir = os.path.dirname(os.path.abspath(__file__))
    project_root = os.path.dirname(script_dir) # Asumiendo que está en /scripts
    
    print(f"Buscando archivos PDF en: {project_root}")
    pdf_list = extract_pdfs(project_root)
    print(f"Se encontraron {len(pdf_list)} archivos PDF.")
    
    # Formatearlo como modulo JS
    js_content = "export const cursos = " + json.dumps(pdf_list, indent=4, ensure_ascii=False) + ";\n"
    
    # Cambiamos las comillas dobles de las keys a formato crudo JS para que se vea mas lindo?
    # En JSON las llaves llevan comillas dobles, en JS no siempre son necesarias, 
    # pero el formato JSON es completamente valido en JS.
    
    output_file = os.path.join(project_root, 'curso.js')
    
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(js_content)
        
    print(f"Archivo generado con éxito: {output_file}")


if __name__ == '__main__':
    main()
