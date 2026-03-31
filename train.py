import hydra


def train_model(cfg):
    pass


@hydra.main(version_base="1.3", config_path="configs", config_name="train")
def main(cfg):
    train_model(cfg)


if __name__ == "__main__":
    main()
