import os
from pathlib import Path

package_name="IncomePrediction"

list_of_files=[
    "github/workflows/.gitkeep",
    f"src/{package_name}/__init__.py",
    f"src/{package_name}/component/__init__.py",
    f"src/{package_name}/component/data_ingestion.py",
    f"src/{package_name}/component/data_transformation.py",
    f"src/{package_name}/component/model_trainer.py",
    f"src/{package_name}/pipeline/__init__.py",
    f"src/{package_name}/pipeline/training_pipeline.py",
    f"src/{package_name}/pipeline/pediction_pipeline.py",
    f"src/{package_name}/utils/__init__.py",
    f"src/{package_name}/utils/utils.py",
    f"src/{package_name}/exception.py",
    f"src/{package_name}/logger.py",
    "notebook/research.ipynb",
    "notebook/data/.gitkeep",
    "setup.py",
    "requirements.txt",
    "init_setup.sh"
]

for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)
 
    if filedir !="":
   
        os.makedirs(filedir,exist_ok=True)
    
    if (not os.path.exists(filepath) or (os.path.getsize(filepath)==0)):
        with open(filepath,"w") as f:
            pass
    else:
        print("FIle already exist")
    