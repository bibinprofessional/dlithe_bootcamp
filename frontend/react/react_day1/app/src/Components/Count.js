import React, { Component } from 'react'

export class Count extends Component {
    constructor(props) {
        super(props);

        this.state =
        {
            count: 0
        };
    }

    handleClick = (e) => {
        this.setState({
            count: this.state.count + 1
        });
    }

    render() {
        return (
            <div>
                <p>{this.state.count}</p>
                <button onClick={this.handleClick}>Count</button>
            </div>

        )
    }
}

export default Count