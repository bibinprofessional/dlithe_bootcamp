import React, { Component } from 'react'

export class GreetClass extends Component {
    constructor(props) {
        super(props);
        this.age = '10';
        this.state =
        {
            name: 'ads',
            age: '21'
        };
    }


    render() {
        return (
            <div>
                hello from class {this.props.age} {this.age} {this.state.age}

            </div>
        )
    }
}

export default GreetClass