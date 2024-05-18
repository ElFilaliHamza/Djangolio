param (
    [string]$task
)

switch ($task) {
    "install" {
        poetry install --no-root
        break
    }
    "update" {
        ./make.ps1 install
        ./make.ps1 migrate
        ./make.ps1 install-precommit
        break
    }
    "run-server" {
        python -m core.manage runserver
        break
    }
    "migrate" {
        python -m core.manage migrate
        break
    }
    "migrates" {
        python -m core.manage makemigrations
        python -m core.manage migrate
        break
    }
    "superuser" {
        python -m core.manage createsuperuser
        break
    }
    "makemigrations"{
        python -m core.manage makemigrations
        python -m core.manage migrate
        break
    }
    "collectstatic" {
        python -m core.manage collectstatic --noinput
        break
    }
    "precommit-all" {
        poetry run pre-commit run --all-files
        break
    }
    "install-precommit" {
        poetry run pre-commit uninstall
        poetry run pre-commit install
        break
    }
    default {
        Write-Output "Unknown task: $task"
        Write-Output "try one of these : install-precommit, precommit-all, collectstatic, makemigrations, superuser,migrates, migrate, run-server,update, install"
        break
    }
}
