def add_noise(data, noise_factor=0.1):
    noise = noise_factor * torch.randn_like(data)
    return data + noise


def get_noisy_data():
    data = torch.rand(1000, 2)
    return add_noise(data)