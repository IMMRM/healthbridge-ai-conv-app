# tests/unit/test_analytics_tool.py

from unittest.mock import MagicMock

from models.claims import Claim
from models.claims_breakup import ClaimsBreakup

from tools.analytics_tool import (
    get_member_claim_frequency,
    get_member_total_claim_amount,
    get_policy_total_claims,
    get_policy_total_claim_amount,
    get_top_hospitals_by_claims,
    get_top_hospitals_by_amount,
    get_high_value_claims,
    get_recent_large_claims,
    get_top_benefit_usage
)


# =====================================================
# TEST 1
# MEMBER CLAIM FREQUENCY
# =====================================================

def test_get_member_claim_frequency():

    mock_db = MagicMock()

    (
        mock_db.query.return_value
        .filter.return_value
        .scalar.return_value
    ) = 4


    result = get_member_claim_frequency(
        mock_db,
        "MEM001"
    )


    assert result["member_id"] == "MEM001"

    assert result["total_claims"] == 4


# =====================================================
# TEST 2
# MEMBER TOTAL CLAIM AMOUNT
# =====================================================

def test_get_member_total_claim_amount():

    mock_db = MagicMock()

    (
        mock_db.query.return_value
        .filter.return_value
        .scalar.return_value
    ) = 250000


    result = get_member_total_claim_amount(
        mock_db,
        "MEM001"
    )


    assert result["member_id"] == "MEM001"

    assert result["total_claim_amount"] == 250000.0


# =====================================================
# TEST 3
# POLICY TOTAL CLAIMS
# =====================================================

def test_get_policy_total_claims():

    mock_db = MagicMock()

    (
        mock_db.query.return_value
        .filter.return_value
        .scalar.return_value
    ) = 7


    result = get_policy_total_claims(
        mock_db,
        "POL001"
    )


    assert result["policy_id"] == "POL001"

    assert result["total_claims"] == 7


# =====================================================
# TEST 4
# POLICY TOTAL CLAIM AMOUNT
# =====================================================

def test_get_policy_total_claim_amount():

    mock_db = MagicMock()

    (
        mock_db.query.return_value
        .filter.return_value
        .scalar.return_value
    ) = 550000


    result = get_policy_total_claim_amount(
        mock_db,
        "POL001"
    )


    assert result["policy_id"] == "POL001"

    assert result["total_claim_amount"] == 550000.0


# =====================================================
# TEST 5
# TOP HOSPITALS BY CLAIMS
# =====================================================

def test_get_top_hospitals_by_claims():

    row = MagicMock()

    row.hospital_name = "Apollo Hospital"

    row.claim_count = 12


    mock_db = MagicMock()

    (
        mock_db.query.return_value
        .group_by.return_value
        .order_by.return_value
        .limit.return_value
        .all.return_value
    ) = [row]


    result = get_top_hospitals_by_claims(
        mock_db
    )


    assert len(result) == 1

    assert result[0]["hospital_name"] == "Apollo Hospital"

    assert result[0]["claim_count"] == 12


# =====================================================
# TEST 6
# TOP HOSPITALS BY AMOUNT
# =====================================================

def test_get_top_hospitals_by_amount():

    row = MagicMock()

    row.hospital_name = "Fortis"

    row.total_amount = 950000


    mock_db = MagicMock()

    (
        mock_db.query.return_value
        .group_by.return_value
        .order_by.return_value
        .limit.return_value
        .all.return_value
    ) = [row]


    result = get_top_hospitals_by_amount(
        mock_db
    )


    assert len(result) == 1

    assert result[0]["hospital_name"] == "Fortis"

    assert result[0]["total_claim_amount"] == 950000.0


# =====================================================
# TEST 7
# HIGH VALUE CLAIMS
# =====================================================

def test_get_high_value_claims():

    claim = Claim()

    claim.claim_id = "CLM100"

    claim.policy_id = "POL010"

    claim.member_id = "MEM020"

    claim.claim_amount = 200000

    claim.approved_amount = 180000

    claim.status = "approved"

    claim.hospital_name = "Medanta"

    claim.claim_type = "cashless"

    claim.claim_date = None


    mock_db = MagicMock()

    (
        mock_db.query.return_value
        .filter.return_value
        .order_by.return_value
        .all.return_value
    ) = [claim]


    result = get_high_value_claims(
        mock_db,
        threshold=100000
    )


    assert len(result) == 1

    assert result[0]["claim_id"] == "CLM100"

    assert result[0]["claim_amount"] == 200000.0


# =====================================================
# TEST 8
# RECENT LARGE CLAIMS
# =====================================================

def test_get_recent_large_claims():

    claim = Claim()

    claim.claim_id = "CLM200"

    claim.policy_id = "POL020"

    claim.member_id = "MEM030"

    claim.claim_amount = 300000

    claim.approved_amount = 250000

    claim.status = "approved"

    claim.hospital_name = "AIIMS"

    claim.claim_type = "reimbursement"

    claim.claim_date = None


    mock_db = MagicMock()

    (
        mock_db.query.return_value
        .order_by.return_value
        .limit.return_value
        .all.return_value
    ) = [claim]


    result = get_recent_large_claims(
        mock_db,
        limit=1
    )


    assert len(result) == 1

    assert result[0]["claim_id"] == "CLM200"


# =====================================================
# TEST 9
# TOP BENEFIT USAGE
# =====================================================

def test_get_top_benefit_usage():

    row = MagicMock()

    row.benefit_type = "ICU"

    row.usage_count = 9


    mock_db = MagicMock()

    (
        mock_db.query.return_value
        .group_by.return_value
        .order_by.return_value
        .limit.return_value
        .all.return_value
    ) = [row]


    result = get_top_benefit_usage(
        mock_db
    )


    assert len(result) == 1

    assert result[0]["benefit_type"] == "ICU"

    assert result[0]["usage_count"] == 9