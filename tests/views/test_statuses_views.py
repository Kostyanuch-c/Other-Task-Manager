from http import HTTPStatus

from django.http import Http404
from django.shortcuts import reverse

import pytest
from tests.factories.statuses import StatusModelFactory
from tests.fixtures.forms.status import status_form_data  # noqa: F401
from tests.fixtures.login_decorator import login_user
from tests.fixtures.services.statuses import status_service  # noqa: F401

from task_manager.tasks.services.status_service import StatusService


def test_get_statuses_without_login(client):
    response = client.get("/statuses/")

    assert response.status_code == HTTPStatus.FOUND

    login_url = reverse("login")
    assert response.url.startswith(login_url)


def test_get_statuses_create_without_login(client):
    response = client.get("/statuses/create/")

    assert response.status_code == HTTPStatus.FOUND

    login_url = reverse("login")
    assert response.url.startswith(login_url)


def test_statuses_update_without_login_and_without_statuses(client):
    response = client.get("statuses/1/update/")
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert "Здесь нет того, что вы ищете" in response.content.decode("utf-8")


def test_statuses_delete_without_login_and_without_statuses(client):
    response = client.get("statuses/1/delete/")
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert "Здесь нет того, что вы ищете" in response.content.decode("utf-8")


@login_user
@pytest.mark.django_db
def test_list_status(
        client,
):
    status = StatusModelFactory.create()
    response = client.get("/statuses/")

    assert response.status_code == HTTPStatus.OK
    assert status.name in response.content.decode("utf-8")


@login_user
@pytest.mark.django_db
def test_status_update_with_login(
        client,
        status_service: StatusService,  # noqa: F811
        status_form_data: dict,  # noqa: F811
):
    status = StatusModelFactory.create()
    response = client.post(
        reverse("status_update", args=[status.id]),
        data=status_form_data,
    )

    assert response.status_code == HTTPStatus.FOUND
    assert response.url.startswith(reverse("status_list"))

    status_after_update = status_service.get_object(status.id)
    assert status_after_update.name == status_form_data["name"]


@login_user
@pytest.mark.django_db
def test_status_delete_with_login(
        client,
        status_service: StatusService,  # noqa: F811
):
    status = StatusModelFactory.create()
    response = client.post(
        reverse("status_delete", args=[status.id]),
    )

    assert response.status_code == HTTPStatus.FOUND
    assert response.url.startswith(reverse("status_list")), f"{response.url}"

    with pytest.raises(Http404):
        status_service.get_object(status.id)


@login_user
@pytest.mark.django_db
def test_create_status(
        client,
        status_service: StatusService,  # noqa: F811
        status_form_data: dict,  # noqa: F811
):
    response = client.post(reverse("status_create"), data=status_form_data)

    assert response.status_code == HTTPStatus.FOUND
    assert response.url.startswith(reverse("status_list"))

    statuses = status_service.get_all_objects()
    assert len(statuses) == 1
