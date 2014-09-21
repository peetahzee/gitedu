/** @jsx React.DOM */

var OrgListRow = React.createClass({
    render: function() {
        console.log(this.props);
        return (<li class="org">{this.props.org.name}</li>);
    }
});

var OrgList = React.createClass({
    render: function() {
        var orgs = [];
        this.props.orgs.forEach(function(org) {
            orgs.push(<OrgListRow org={org} key={org.name} />);
        });
        return (
            <div>
                <h2>organizations</h2>
                <ul>{orgs}</ul>
            </div>
        );
    }
});

$(document).ready(function() {
    $.getJSON('/gh/user/orgs').done(function(json) {
        orgs = [];
        json.forEach(function(org) {
            orgs.push({name: org.login, id: org.id })
        });

        React.renderComponent(<OrgList orgs={orgs} />, $('#left_container')[0]);
    })
})

