import wandb
wandb.init(entity='rmh-awasthi', project='demo_project')
art = wandb.Artifact('NYC-Taxi', type='preprocessed_dataset')
# ... add content to artifact ...
wandb.log_artifact(art)