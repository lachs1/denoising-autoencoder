# denoising-autoencoder
Denoising autoencoder for ECG signals


This study aims to implement and train a neural network-based filtering technique using a denoising autoencoder. An autoencoder is a special neural network trained to copy its input to its output, and they are often used for data compression. However, the model can also be trained to perform denoising by training the autoencoder using a corrupted signal as input, and the original signal as the target. Thus, by feeding a noisy ECG signal to the autoencoder, the model should be able to reconstruct the original signal.

