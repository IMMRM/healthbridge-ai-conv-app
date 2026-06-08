from unittest.mock import MagicMock

from models.plan_benefits import PlanBenefit

from tools.benefits_tool import (
    get_benefit_by_id,
    get_plan_benefits,
    get_benefits_by_type,
    check_benefit_coverage,
    get_coverage_limit
)


# =====================================================
# TEST 1
# GET BENEFIT BY ID
# =====================================================

def test_get_benefit_by_id():

    benefit = PlanBenefit()

    benefit.benefit_id = "BEN001"
    benefit.plan_id = "STAR"

    benefit.benefit_type = "ROOM_RENT"
    benefit.sub_type = "PRIVATE_ROOM"

    benefit.coverage_limit = 5000
    benefit.waiting_period = 0

    benefit.is_covered = True
    benefit.remarks = "Covered"


    mock_db = MagicMock()

    (
        mock_db.query.return_value
        .filter.return_value
        .first.return_value
    ) = benefit


    result = get_benefit_by_id(
        mock_db,
        "BEN001"
    )


    assert result["benefit_id"] == "BEN001"

    assert result["benefit_type"] == "ROOM_RENT"

    assert result["coverage_limit"] == 5000.0


# =====================================================
# TEST 2
# GET PLAN BENEFITS
# =====================================================

def test_get_plan_benefits():

    benefit1 = PlanBenefit()

    benefit1.benefit_id = "BEN001"
    benefit1.plan_id = "STAR"
    benefit1.benefit_type = "ROOM_RENT"


    benefit2 = PlanBenefit()

    benefit2.benefit_id = "BEN002"
    benefit2.plan_id = "STAR"
    benefit2.benefit_type = "ICU"


    mock_db = MagicMock()

    (
        mock_db.query.return_value
        .filter.return_value
        .all.return_value
    ) = [benefit1, benefit2]


    result = get_plan_benefits(
        mock_db,
        "STAR"
    )


    assert len(result) == 2

    assert result[0]["benefit_id"] == "BEN001"

    assert result[1]["benefit_id"] == "BEN002"


# =====================================================
# TEST 3
# GET BENEFITS BY TYPE
# =====================================================

def test_get_benefits_by_type():

    benefit = PlanBenefit()

    benefit.benefit_id = "BEN003"

    benefit.plan_id = "STAR"

    benefit.benefit_type = "ICU"


    mock_db = MagicMock()

    (
        mock_db.query.return_value
        .filter.return_value
        .all.return_value
    ) = [benefit]


    result = get_benefits_by_type(
        mock_db,
        "STAR",
        "ICU"
    )


    assert len(result) == 1

    assert result[0]["benefit_type"] == "ICU"


# =====================================================
# TEST 4
# CHECK BENEFIT COVERAGE
# =====================================================

def test_check_benefit_coverage():

    benefit = PlanBenefit()

    benefit.is_covered = True


    mock_db = MagicMock()

    (
        mock_db.query.return_value
        .filter.return_value
        .first.return_value
    ) = benefit


    result = check_benefit_coverage(
        mock_db,
        "STAR",
        "ROOM_RENT"
    )


    assert result is True


# =====================================================
# TEST 5
# CHECK BENEFIT NOT COVERED
# =====================================================

def test_check_benefit_not_covered():

    benefit = PlanBenefit()

    benefit.is_covered = False


    mock_db = MagicMock()

    (
        mock_db.query.return_value
        .filter.return_value
        .first.return_value
    ) = benefit


    result = check_benefit_coverage(
        mock_db,
        "HERO",
        "MATERNITY"
    )


    assert result is False


# =====================================================
# TEST 6
# GET COVERAGE LIMIT
# =====================================================

def test_get_coverage_limit():

    benefit = PlanBenefit()

    benefit.coverage_limit = 10000


    mock_db = MagicMock()

    (
        mock_db.query.return_value
        .filter.return_value
        .first.return_value
    ) = benefit


    result = get_coverage_limit(
        mock_db,
        "SUPERSTAR",
        "ICU"
    )


    assert result == 10000.0


# =====================================================
# TEST 7
# GET COVERAGE LIMIT NULL
# =====================================================

def test_get_coverage_limit_none():

    benefit = PlanBenefit()

    benefit.coverage_limit = None


    mock_db = MagicMock()

    (
        mock_db.query.return_value
        .filter.return_value
        .first.return_value
    ) = benefit


    result = get_coverage_limit(
        mock_db,
        "SUPERSTAR",
        "ICU"
    )


    assert result is None