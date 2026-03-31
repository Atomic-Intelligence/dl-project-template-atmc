import hydra


def test_model(cfg):
    pass


@hydra.main(version_base="1.3", config_path="configs", config_name="test")
def main(cfg):
    test_model(cfg)


if __name__ == "__main__":
    main()
