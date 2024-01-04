import React, { Component } from 'react'

export class Message extends Component {
    constructor() {
        super()

        this.state = {
            Message: 'welcome user'
        }
    }

    changeMessage = () => {
        this.setState({ Message: 'Thankyou!' })
    }

    render() {
        return (
            <div>
                <h1>{this.state.Message}</h1>
                <button onClick={this.changeMessage}>Subscribe</button>
                <br />
                <br />
                <br />
            </div>
        )
    }
}

export default Message