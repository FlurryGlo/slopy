from slobypy.app import SlApp
from slobypy.react import *
from slobypy.react.component import *
from slobypy.rpc import *

app = SlApp()


@app.component("/route1")
class MyComponent1(Component):

    def name(self):
        return "test"

    def body(self):
        yield P("test")
        yield MyComponent2(props={"test_prop_value": "the test value"})

    def mount(self):
        pass


class MyComponent2(Component):
    def name(self):
        return "test"

    def body(self):
        yield P(self.props["test_prop_value"])

    def mount(self):
        print("test prop:", self.props["test_prop_value"])


@app.component("secondcomponent/fake")
class FakeComponent(Component):
    def name(self):
        return "im a fake"

    def body(self):
        yield P("this is a fake prop, something is wrong, this shouldnt be rendered!")

    def mount(self):
        print("bad run")


r = RPC(app)
