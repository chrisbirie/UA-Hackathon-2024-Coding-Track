FROM python:3
ENV PYTHONPATH="./code" 
#create a working directory in the virtual machine (VM)
WORKDIR /code    

# copy all the python requirements stored in requirements.txt into the new directoy (in the VM)
COPY ./requirements.txt /code/requirements.txt    

# copy all files to the new directory (in the VM)
COPY ./ /code/

# run the pip install for packages
RUN pip install requests
RUN pip install openpyxl


CMD [ "python", "./code/scripts/hackathon_scoring_script.py" ]