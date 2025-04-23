# Image Representation and Classification with Autoencoder, ResNet50, and CLIP

This project explores the impact of different image representations on the accuracy of a simple 3-NN classifier. The dataset used is a subset of CIFAR-100 (10 classes), and the representations include:

- **Raw pixel vectors**
- **Latent space from a Convolutional Autoencoder**
- **Pretrained ResNet50 embeddings**
- **OpenAI CLIP (ViT-B/32) embeddings**

The goal is to compare classification accuracy across these feature spaces and highlight the importance of good representation for even simple classifiers.

## 📊 Summary of Results

| Representation Space       | Description                                       | 3-NN Accuracy |
|----------------------------|---------------------------------------------------|---------------|
| Raw Image Space            | Flattened 32×32×3 vectors                         | 35.60%        |
| Autoencoder Latent Space   | 512-dim compressed features (4×4×32)              | 44.30%        |
| ResNet50 Embeddings        | 2048-dim features (ImageNet pretrained)          | 88.10%        |
| CLIP Embeddings (ViT-B/32) | 512-dim multimodal features from image-text model| 92.60%        |

## 📁 Dataset

- **CIFAR-100** (from TensorFlow datasets)
- 10 selected classes (e.g., `bowl`, `bus`, `butterfly`, etc.)
- 600 images per class: 500 for training, 100 for testing

## 🧠 Models and Methods

### 🔹 1. Convolutional Autoencoder

A custom CAE architecture was designed with 3 convolutional blocks in the encoder and mirrored decoder structure. The latent space had shape 4×4×32 (512 features). Only the encoder was used to generate features for classification.

- **Loss**: Mean Squared Error (MSE)
- **Optimizer**: Adam (lr = 0.001)
- **Training**: 50 epochs, batch size = 8
- **Latent Space Accuracy**: **44.30%**

### 🔹 2. ResNet50 Embeddings

Pretrained ResNet50 was used without its top layer and with global average pooling. Images were resized to 224×224 and normalized.

- **Output Vector Size**: 2048
- **3-NN Accuracy**: **88.10%**

### 🔹 3. CLIP (ViT-B/32) Embeddings

Using OpenAI’s CLIP model in PyTorch, each image was passed through the ViT-B/32 image encoder. The output embeddings were normalized and used with 3-NN.

- **Output Vector Size**: 512
- **3-NN Accuracy**: **92.60%**

## 🧪 Evaluation

The 3-Nearest Neighbors classifier was used consistently across all representations to isolate the effect of the feature space.

- Distance metric: Euclidean
- Accuracy metric: Classification accuracy on test set
## 📈 Visualization with t-SNE

To better understand how each type of image representation separates the different classes in feature space, **t-SNE** was used to reduce the high-dimensional vectors to 2D.

Four 2D scatter plots were generated for:

1. **Raw Image Space** (flattened pixel vectors)
2. **Autoencoder Latent Space**
3. **ResNet50 Embeddings**
4. **CLIP Embeddings**

Each plot visualizes the training set in 2D with color-coded class labels. As expected:

- **Raw pixel features** produce poor separation.
- **Autoencoder representations** form somewhat better clusters.
- **ResNet50 and CLIP embeddings** show clear, tight clustering by class — confirming their strong semantic encoding power.

This visual comparison highlights how **better feature representations** lead to **better class separability**, even for simple classifiers like 3-NN.

> ✅ Technique: `sklearn.manifold.TSNE` with `perplexity=30` and `random_state=42`

## 🛠️ Technologies Used

- Python, TensorFlow, PyTorch
- OpenAI CLIP model
- Scikit-learn (3-NN classifier)
- NumPy, Matplotlib, PIL

## 📚 References
- Masci, J., Meier, U., Cireşan, D., & Schmidhuber, J. (2011). [Stacked Convolutional Auto-Encoders for Hierarchical Feature Extraction](https://people.idsia.ch/~ciresan/data/icann2011.pdf). 
- He, K., Zhang, X., Ren, S., & Sun, J. (2016). [Deep Residual Learning for Image Recognition](https://arxiv.org/abs/1512.03385).
- Radford, A. et al. (2021). [Learning Transferable Visual Models From Natural Language Supervision (CLIP)](https://arxiv.org/abs/2103.00020). arXiv:2103.00020.




