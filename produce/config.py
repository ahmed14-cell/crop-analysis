from pathlib import Path


class Config:
    random_state = 42
    assets_path = Path('./assets')
    original_data_path = assets_path / 'datasets' / 'dataset1.csv'
    dataset_path = assets_path / 'data'
    features_path = assets_path / 'features'
    models_path = assets_path / 'models'
    metrics_file_path = assets_path / 'metrics.json'
