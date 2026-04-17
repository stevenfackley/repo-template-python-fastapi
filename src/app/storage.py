"""S3-compatible object storage client (Cloudflare R2 prod, MinIO local).

Lazy — configured on first use. Raises `RuntimeError` if env is missing.
"""

from __future__ import annotations

import os
from functools import lru_cache

import boto3
from botocore.client import BaseClient
from botocore.config import Config


@lru_cache(maxsize=1)
def get_s3() -> BaseClient:
    endpoint = os.environ.get("S3_ENDPOINT")
    key = os.environ.get("S3_ACCESS_KEY_ID")
    secret = os.environ.get("S3_SECRET_ACCESS_KEY")
    if not endpoint or not key or not secret:
        raise RuntimeError(
            "S3 env not configured (S3_ENDPOINT/S3_ACCESS_KEY_ID/S3_SECRET_ACCESS_KEY)"
        )

    return boto3.client(
        "s3",
        endpoint_url=endpoint,
        region_name=os.environ.get("S3_REGION", "auto"),
        aws_access_key_id=key,
        aws_secret_access_key=secret,
        config=Config(
            s3={"addressing_style": "path" if os.environ.get("S3_FORCE_PATH_STYLE") == "true" else "auto"},
            signature_version="s3v4",
        ),
    )


def get_bucket() -> str:
    bucket = os.environ.get("S3_BUCKET")
    if not bucket:
        raise RuntimeError("S3_BUCKET is not set")
    return bucket


PUBLIC_BASE_URL = os.environ.get("S3_PUBLIC_BASE_URL", "")
