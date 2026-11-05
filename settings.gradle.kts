pluginManagement {
    repositories {
        google {
            content {
                includeGroupByRegex("com\\.android.*")
                includeGroupByRegex("com\\.google.*")
                includeGroupByRegex("androidx.*")
            }
        }
        mavenCentral()
        gradlePluginPortal()
    }
}
dependencyResolutionManagement {
    repositoriesMode.set(RepositoriesMode.FAIL_ON_PROJECT_REPOS)
    repositories {
        google()
        mavenCentral()
        // Huawei Health Kit (steps from Huawei Health) and the HMS Core libraries it stands on.
        maven("https://developer.huawei.com/repo/") {
            content {
                includeGroupByRegex("com\\.huawei.*")
            }
        }
    }
}

rootProject.name = "Lipovka"
include(":app")
