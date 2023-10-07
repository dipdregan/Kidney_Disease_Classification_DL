epoch [$(date)] : "Starting local setup like creating Env and Installments" 
echo [$(date)] : "Creating python Env.....>>>>"
conda create --prefix ./env python=3.8 -y
echo [$(date)] : "Env created ,Let's activate the env"
conda activate env/
echo [$(date)] : "Installing the Enviroments"
pip install -r requirements_dev.txt
echo [$(date)] : "==============>>>>>>>Setup completed <<<<<<=========== !"

# for runing the the script run in terminal "bash init_setup.sh"
