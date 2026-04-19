from .belebele import BelebeleBenchmark
from .mgsm import MGSMBenchmark
from .include import INCLUDEBenchmark
from .blend import BLEnDBenchmark
from .indicgenbench import IndicGenBenchBenchmark
from .global_mmlu import GlobalMMLUBenchmark
from .milu import MILUBenchmark

BENCHMARKS = {
    "belebele": BelebeleBenchmark,
    "mgsm": MGSMBenchmark,
    "include": INCLUDEBenchmark,
    "blend": BLEnDBenchmark,
    "indicgenbench": IndicGenBenchBenchmark,
    "global_mmlu": GlobalMMLUBenchmark,
    "milu": MILUBenchmark,
}

__all__ = [
    "BelebeleBenchmark",
    "MGSMBenchmark",
    "INCLUDEBenchmark",
    "BLEnDBenchmark",
    "IndicGenBenchBenchmark",
    "GlobalMMLUBenchmark",
    "MILUBenchmark",
    "BENCHMARKS",
]
