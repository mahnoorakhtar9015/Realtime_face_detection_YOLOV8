
def run_inference(model, frame, conf_threshold: float):
    results = model.predict(frame, conf=conf_threshold)
    return results[0].plot()
