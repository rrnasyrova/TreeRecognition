import torch.nn.functional as F
import torch
import torchvision.transforms as transforms

class Predictor:
    def __init__(self, model_path):
        self._device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
        self.model_path = model_path
        self.model = torch.load(self.model_path, map_location=self._device)
        self.model.to(self._device)
        self.model.eval()

    def process_image(self, image_from_gui):

        transformation = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        ])

        processed_image = transformation(image_from_gui).unsqueeze(0).to(self._device)

        return processed_image

    def predict(self, image_from_gui):
        image = self.process_image(image_from_gui)
        output = self.model(image)
        probabilities = F.softmax(output, dim=1)
        probabilities = probabilities.squeeze().tolist()

        class_probabilities = {i: prob * 100 for i, prob in enumerate(probabilities)}

        class_probabilities_sorted = dict(sorted(class_probabilities.items(), key=lambda x: x[1], reverse=True)[:3])
        return class_probabilities_sorted