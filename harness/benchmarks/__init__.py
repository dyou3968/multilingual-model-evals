from .belebele import BelebeleBenchmark
from .mgsm import MGSMBenchmark
from .include import INCLUDEBenchmark
from .blend import BLEnDBenchmark
from .indicgenbench import IndicGenBenchBenchmark

BENCHMARKS = {
    "belebele": BelebeleBenchmark,
    "mgsm": MGSMBenchmark,
    "include": INCLUDEBenchmark,
    "blend": BLEnDBenchmark,
    "indicgenbench": IndicGenBenchBenchmark,
}

__all__ = [
    "BelebeleBenchmark",
    "MGSMBenchmark",
    "INCLUDEBenchmark",
    "BLEnDBenchmark",
    "IndicGenBenchBenchmark",
    "BENCHMARKS",
]
