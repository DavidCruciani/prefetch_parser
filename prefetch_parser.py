# coding: utf-8
import json
import argparse
from pathlib import Path

import pyscca


def prefetch2json(filepath: str) -> dict:
    """Convert prefetch to json.
    Args:
        filepath (str): Input Prefetch(.pf) file.
    Note:
        Since the content of the file is loaded into memory at once,
        it requires the same amount of memory as the file to be loaded.
    """

    p = pyscca.file()
    p.open_file_object(Path(filepath).open(mode='rb'))

    result = {
        'name': p.executable_filename,
        'filenames': [name for name in p.filenames],
        'exec_count': p.run_count,
        'last_exec_time': p.get_last_run_time(0).strftime("%Y-%m-%d %H:%M:%S"),
        'format_version': p.format_version,
        'prefetch_hash': p.prefetch_hash,
        'metrics': [
            {
                'filename': metrics.filename,
                'file_reference': metrics.file_reference,
            } for metrics in p.file_metrics_entries
        ],
        'volumes': [
            {
                'path': volume.device_path,
                'creation_time': volume.get_creation_time().strftime("%Y-%m-%d %H:%M:%S"),
                'serial_number': volume.serial_number,
            } for volume in p.volumes
        ],
    }

    p.close()

    return result
    


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--prefetchfile", type=Path, help="Windows Prefetch file.")
    parser.add_argument("-o", "--jsonfile", type=Path, help="Output json file path. '-' will print command output on terminal.")
    args = parser.parse_args()

    # Convert prefetch to json file.
    print(f"******** Converting {args.prefetchfile} ********")
    if not args.jsonfile.name == "-":
        o = Path(args.jsonfile)
        o.write_text(
            json.dumps(
                prefetch2json(filepath=args.prefetchfile),
                indent=2
            )
        )
    else:
        print( 
            json.dumps(
                prefetch2json(filepath=args.prefetchfile),
                indent=2
            )
        )
