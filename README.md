
# Room mapping and Image generation app

Left side bad has 2 options
Tab 1 is Room Mapping it takes two input files and finds matching attribues in room description form the given attribues dict (sample file in example_input_files folder)

After loading data can select 1 value each for different type of attribues.

Now can go to Tab 2 Content generation it will have 3 dropdowns, one for photo style and remaing two for using attribues selected in previous screen to generate prompt message

On clicking generate button it will show a message and call the segmind api with the prompt message, please wait for it to get response, then it will show the Image on the screen with caption.


## Deployment

To run this project using docker run from the main directory having Dockerfile
```bash
docker build -t streamlit-app .

docker run -p 8501:8501 streamlit-app
```
and visit http://localhost:8501/ in browser to open


Or to run directly, CD to root directory of this repo folder
```bash
streamlit run source/app.py
```
and visit http://localhost:8501/ in browser to open
