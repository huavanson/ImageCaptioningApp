> forked from: [react-file-input](https://github.com/Data-Meister/react-file-input)
> ad pushed to npm as `react-input-file` because the original does not support react 15.x as peer dependency and pull requests are not accepted so far.

react-input-file
============
[Demo](https://captivationsoftware.github.io/react-input-file)

Styling native HTML file inputs can be a pretty big pain, and to make matters worse, the browser default look-and-feel is probably at odds with your app's design. This problem is what react-input-file aims to solve.

Once integrated, react-input-file quickly eliminates the headaches associated with forms requiring file upload.

## Installation
```sh
npm install react-input-file
```

## Code Example
Usage is pretty simple: just use react-input-file instead of `<input type="file" />`!

app.jsx
```js
var React = require('react'),
  FileInput = require('react-input-file');

var Form = React.createClass({
  handleChange: function(event) {
    console.log('Selected file:', event.target.files[0]);
  },

  render: function() {
    return (
      <form>
        <FileInput name="myImage"
                   accept=".png,.gif"
                   placeholder="My Image"
                   className="inputClass"
                   onChange={this.handleChange} />
      </form>
    );
  },
});

```

The list of valid props can be found below.

### Props

#### name, accept, className, placeholder, onChange
Behave just like standard react-style attributes on input controls.

## Contributors

Captivation Software (@teamcaptivation)

By all means, if you see room for improvement, let us know!


## License

MIT License
