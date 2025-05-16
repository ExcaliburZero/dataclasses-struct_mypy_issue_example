from typing import IO

import dataclasses_struct as dcs


@dcs.dataclass()
class MyClass:
    a: dcs.U16

    def write_bin(self, output_stream: IO[bytes]) -> None:
        output_stream.write(self.pack())
