import os
import yaml
from pathlib import Path
from typing import Any, Dict, Optional


def read_yaml(file_path: str, env_substitution: bool = False) -> Dict[str, Any]:
    """
    Read a YAML file and return its contents as a dictionary.
    
    Args:
        file_path: Path to the YAML file
        env_substitution: If True, substitute environment variables in values
        
    Returns:
        Dictionary containing the parsed YAML data
        
    Raises:
        FileNotFoundError: If the YAML file doesn't exist
        yaml.YAMLError: If the YAML is malformed
    """
    try:
        # Convert to absolute path if needed
        yaml_file = Path(file_path)
        
        if not yaml_file.exists():
            raise FileNotFoundError(f"YAML file not found: {file_path}")
        
        with open(yaml_file, 'r', encoding='utf-8') as f:
            data = yaml.safe_load(f)
        
        if env_substitution and data:
            data = _substitute_env_vars(data)
        
        return data or {}
    
    except yaml.YAMLError as e:
        raise yaml.YAMLError(f"Error parsing YAML file {file_path}: {str(e)}")
    except Exception as e:
        raise Exception(f"Error reading YAML file {file_path}: {str(e)}")


def _substitute_env_vars(data: Any) -> Any:
    """
    Recursively substitute environment variables in the data.
    Supports ${VAR_NAME} or ${VAR_NAME:-default_value} syntax.
    """
    if isinstance(data, dict):
        return {key: _substitute_env_vars(value) for key, value in data.items()}
    elif isinstance(data, list):
        return [_substitute_env_vars(item) for item in data]
    elif isinstance(data, str):
        return _replace_env_vars_in_string(data)
    else:
        return data


def _replace_env_vars_in_string(value: str) -> str:
    """Replace environment variables in a string."""
    import re
    
    def replace_var(match):
        var_name = match.group(1)
        default = None
        
        if ':-' in var_name:
            var_name, default = var_name.split(':-', 1)
        
        return os.getenv(var_name, default or match.group(0))
    
    # Pattern to match ${VAR_NAME} or ${VAR_NAME:-default}
    pattern = r'\$\{([^}]+)\}'
    return re.sub(pattern, replace_var, value)


if __name__ == "__main__":
    # Example usage
    config = read_yaml('config/db_details.yaml', env_substitution=True)
    print(config)
