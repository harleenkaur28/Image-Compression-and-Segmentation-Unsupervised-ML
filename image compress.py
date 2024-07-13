from flask import Flask, request, render_template, send_file 
import numpy as np
import matplotlib as mpl
from sklearn.cluster import KMeans
from kneed import KneeLocator
import cv2
import io

def compressFileAuto(img_path):
    img = mpl.image.imread(img_path)
    
    if len(img.shape) == 2:
        # Grayscale image
        height, width = img.shape
        X = img.reshape(-1, 1)
    else:
        # Color image
        height, width, _ = img.shape
        X = img.reshape(-1, 3)
    wcss=[]
    for i in range(1,11):
         kmeans = KMeans(n_clusters=i, init='k-means++')
         kmeans.fit(X)
         wcss.append(kmeans.inertia_)
    if len(range(1, 11)) == len(wcss):
         knee = KneeLocator(range(1, 11), wcss, curve='convex', direction='decreasing')
    n = knee.knee if knee.knee else 1 
    kmeans=KMeans(n_clusters=n, init='k-means++')
    kmeans.fit(X)

    new_img = kmeans.cluster_centers_[kmeans.labels_]
    new_img = (new_img).astype(np.uint8)
    if len(img.shape) == 2:
        # Grayscale image
        new_img = new_img.reshape((height, width))
    else:
        # Color image
        new_img = new_img.reshape((height, width, 3))

    return new_img

def compressFile(n, img_path):
    img = mpl.image.imread(img_path)

    if len(img.shape) == 2:
        # Grayscale image
        height, width = img.shape
        X = img.reshape(-1, 1)
    else:
        # Color image
        height, width, _ = img.shape
        X = img.reshape(-1, 3)

    kmeans = KMeans(n_clusters=n, init='k-means++')
    kmeans.fit(X)

    new_img = kmeans.cluster_centers_[kmeans.labels_]
    new_img = (new_img).astype(np.uint8)
    if len(img.shape) == 2:
        # Grayscale image
        new_img = new_img.reshape((height, width))
    else:
        # Color image
        new_img = new_img.reshape((height, width, 3))

    return new_img
          
app=Flask(__name__)
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    select_file_message=""
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            select_file_message = "No File Selected"
        if file:
            number = request.form.get("number")
            if number=="":
                 compressed_img = compressFileAuto(file)
            else:
                compressed_img= compressFile(int(number), file)
            select_file_message = "File Uploaded Successfully"
            compressed_img_bytes = cv2.imencode('.jpeg', cv2.cvtColor(compressed_img, cv2.COLOR_RGB2BGR))[1].tobytes()
            return send_file(io.BytesIO(compressed_img_bytes), mimetype='image/jpeg', as_attachment=True, download_name='compressed_image.jpeg')
    return render_template('upload.html', select_file=select_file_message)
   
    
if __name__ == '__main__':
    app.run(debug=True)
