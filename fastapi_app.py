from fastapi import FastAPI
from fastapi.requests import Request
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import markdown
import os
# import jinja2
import frontmatter
# import datetime

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

def read_md_file(file_path):
    with open(file_path, 'r') as f:
    #     content = f.read()
    # return content
        post = frontmatter.load(f)
    return post



@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    files = os.listdir('posts')  # Assuming your posts are in a directory named 'posts'
    # links = [f'<a href="/post/{f}">{f}</a><br/>' for f in files]
    posts = []
    for f in files:
        post = read_md_file(f'posts/{f}')
        title = post.metadata.get('title', f)  # Use the file name as a fallback if the title is not available
        date = post.metadata.get('date', '2021-01-01')  # Use a default date if the date is not available')
        posts.append({'title': title, 'file': f, 'date': date})
        # print(post.metadata)
    
    # Sort the posts by date in descending order (newest first)
    posts.sort(key=lambda x: x['date'], reverse=True)
    
    return templates.TemplateResponse("index.html", {"request": request, "posts": posts})

@app.get("/post/{post_name}", response_class=HTMLResponse)
def read_post(request: Request, post_name: str):
    post = read_md_file(f'posts/{post_name}')
    html_content = markdown.markdown(post.content)
    title = post.metadata.get('title', post_name)  # Use the file name as a fallback if the title is not available
    date = post.metadata.get('date', '2021-01-01')  # Use a default date if the date is not available
    tags = post.metadata.get('tags', [])  # Use an empty list as a fallback if the tags are not available
    return templates.TemplateResponse("post.html", {"request": request, "content": html_content, "title": title, "date": date, "tags": tags})

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
    