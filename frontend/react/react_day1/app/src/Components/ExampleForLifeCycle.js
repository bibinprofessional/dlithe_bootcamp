import React, { Component } from 'react'

export class ExampleForLifeCycle extends Component {
    constructor(props) {
        super(props)

        this.state = {
            count: 0,
            count2: 0
        };
        console.log('Constructor')
    }
    componentDidMount() {
        console.log('mount');
    }
    componentDidUpdate() {
        console.log('update');
    }
    componentWillUnmount() {
        console.log('unmount')
    }

    increment_count = () => {
        this.setState({
            count: this.state.count + 1
        })
    }
    increment_count2 = () => {
        this.setState({
            count2: this.state.count2 + 1
        })
    }
    render() {
        return (
            <div>
                <h2>{this.state.count}</h2>
                <button onClick={this.increment_count}>Count</button>
                <h2>{this.state.count2}</h2>
                <button onClick={this.increment_count2}>Count2</button>
            </div>
        )
    }
}

export default ExampleForLifeCycle