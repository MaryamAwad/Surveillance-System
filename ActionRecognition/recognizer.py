import torch

class ActionRecognizer:
    
    def recognize_action(self, model,device,frames):
        model.eval()
        with torch.no_grad():
            frames = [frame.to(device) for frame in frames]
            output = model(frames.unsqueeze(0))
            _,prediction = torch.max(output,1)
            if prediction==1:
                return 1
            else:
                return 0
        