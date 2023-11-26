# Use an official Python runtime as a parent image
FROM python:3.12

# Set the working directory in the container
WORKDIR /root

# Copy the requirements file into the container at /root
COPY requirements.txt .

# Force install pip if some issue
# RUN python3 -m pip install --force-reinstall --upgrade pip

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /root
COPY . .

# EXPOSE 8080

# Command to run your Streamlit app
CMD ["streamlit", "run", "source/app.py"]
