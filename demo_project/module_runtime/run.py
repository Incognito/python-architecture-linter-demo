from demo_project.module_runtime.provider import RuntimeProvider

if __name__ == "__main__":
    provider = RuntimeProvider()
    runtime = provider.provide_runtime()
    runtime.run()
