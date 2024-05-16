from dataclasses import dataclass

@dataclass
class TrainConfig:
    img_list_path: str
    subset_size: int
    batch_size: int
    n_epochs: int
    log_every: int