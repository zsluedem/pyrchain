from typing import List
from dataclasses import dataclass, field

from .meta import from_pb

@from_pb
@dataclass
class DeployInfo:
    deployer: str
    term: str
    timestamp: int
    sig: str
    sigAlgorithm: str
    phloPrice: int
    phloLimit: int
    validAfterBlockNumber: int
    cost: int
    errored: bool
    systemDeployError: str

@from_pb
@dataclass
class BondInfo:
    validator: str
    stake: int

@from_pb
@dataclass
class LightBlockInfo:
    # BlockMessageProto
    blockHash: str
    sender: str
    seqNum: int
    sig: str
    sigAlgorithm: str
    shardId: str
    extraBytes: bytes

    # HeaderProto
    version: int
    timestamp: int
    headerExtraBytes: bytes
    parentsHashList: List[str]

    # BodyProto
    blockNumber: int
    preStateHash: str
    postStateHash: str
    bodyExtraBytes: bytes

    # extra
    blockSize: str
    deployCount: int
    faultTolerance: float
    BondInfo: List[BondInfo] = field(default_factory=BondInfo)

@from_pb
@dataclass
class BlockInfo:
    blockInfo: LightBlockInfo = field(default_factory=LightBlockInfo)
    deploys: List[DeployInfo] = field(default_factory=DeployInfo)