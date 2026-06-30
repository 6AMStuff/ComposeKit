import argparse
import tempfile
import unittest
from pathlib import Path
from typing import Any
from unittest.mock import MagicMock

import yaml

from composekit.generate import (
    Config,
    capitalize_name,
    duplicate_entries,
    generate,
    get_folder_name,
    handle_volumes,
    is_custom_bind,
    main,
)


def make_mock_config(bind_path: str = "/bind") -> Config:
    config = MagicMock(spec=Config)
    config.__getitem__.side_effect = lambda key: {
        "bind_path": bind_path,
        "use_full_directory": True,
        "capitalize_folder_name": False,
        "restart_policy": "unless-stopped",
        "network_name": "cloud",
    }[key]
    return config


class TestGenerate(unittest.TestCase):
    def test_is_custom_bind(self) -> None:
        self.assertTrue(is_custom_bind("/volume:rw;config"))
        self.assertFalse(is_custom_bind("/volume:/container"))
        self.assertTrue(is_custom_bind("/volume"))

    def test_handle_volumes_basic(self) -> None:
        config = make_mock_config()
        volumes = ["/volume", "/volume2"]
        container: dict[str, Any] = {}
        folder = get_folder_name("container", container, config)
        result = handle_volumes(config, folder, volumes, [])
        expected = [
            "/bind/container/volume:/volume",
            "/bind/container/volume2:/volume2",
        ]
        self.assertEqual(result, expected)

    def test_handle_volumes_with_custom_binds(self) -> None:
        config = make_mock_config()
        volumes = ["/volume:/volume", "/volume2:/volume2"]
        container: dict[str, Any] = {}
        folder = get_folder_name("container", container, config)
        result = handle_volumes(config, folder, volumes, [])
        self.assertEqual(result, ["/volume:/volume", "/volume2:/volume2"])

    def test_handle_volumes_with_mount_options_and_custom_name(self) -> None:
        config = make_mock_config()
        volumes = ["/volume:ro;config", "/volume2:rw;data"]
        container: dict[str, Any] = {}
        folder = get_folder_name("container", container, config)
        result = handle_volumes(config, folder, volumes, [])
        self.assertEqual(
            result,
            [
                "/bind/container/config:/volume:ro",
                "/bind/container/data:/volume2:rw",
            ],
        )

    def test_duplicate_entries(self) -> None:
        devices = ["/device", "/device2:/device2"]
        result = duplicate_entries(devices)
        self.assertEqual(result, ["/device:/device", "/device2:/device2"])

    def test_capitalize_name(self) -> None:
        self.assertEqual(capitalize_name("docker"), "Docker")
        self.assertEqual(capitalize_name("D"), "D")

    def test_generate_minimal(self) -> None:
        config = make_mock_config()
        container = {"image": "nginx"}
        result = generate("web", container, config)
        self.assertEqual(result["image"], "nginx")
        self.assertEqual(result["hostname"], "web")
        self.assertEqual(result["container_name"], "web")
        self.assertEqual(result["restart"], "unless-stopped")
        self.assertEqual(result["networks"], ["cloud"])

    def test_main_handles_duplicate_containers_without_folder(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            containers = root / "containers"
            composes = root / "composes"
            output = root / "docker-compose.yaml"
            containers.mkdir()
            (containers / "container.yaml").write_text(
                "image: nginx\n---\nimage: redis\n"
            )

            args = argparse.Namespace(
                config=None,
                containers=str(containers),
                composes=str(composes),
                output=str(output),
                commit=False,
            )

            main(args)

            compose = yaml.safe_load((composes / "container.yaml").read_text())
            self.assertEqual(
                list(compose["services"].keys()), ["container", "container_2"]
            )

    def test_handle_volumes_with_full_capitalize(self) -> None:
        config = Config()
        config["bind_path"] = "${BIND_PATH}"
        config["capitalize_folder_name"] = "full"
        volumes = ["/volume", "/volume2"]
        container: dict[str, Any] = {}
        folder = get_folder_name("container", container, config)
        result = handle_volumes(config, folder, volumes, [])
        self.assertEqual(
            result,
            [
                "${BIND_PATH}/Container/volume:/volume",
                "${BIND_PATH}/Container/volume2:/volume2",
            ],
        )

    def test_handle_volumes_with_non_custom_capitalize(self) -> None:
        config = Config()
        config["bind_path"] = "${BIND_PATH}"
        config["capitalize_folder_name"] = "non_custom"
        volumes = ["/volume", "/volume2"]
        container: dict[str, Any] = {"folder": "container"}
        folder = get_folder_name("container", container, config)
        result = handle_volumes(config, folder, volumes, [])
        self.assertEqual(
            result,
            [
                "${BIND_PATH}/container/volume:/volume",
                "${BIND_PATH}/container/volume2:/volume2",
            ],
        )
