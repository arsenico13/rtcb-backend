# -*- coding: utf-8 -*-
from .schema import Match, Tournament
from .service import TournamentService

import graphene


class CreateMatch(graphene.ClientIDMutation):
    """ Crezione di una nuova partita """

    class Input:
        location = graphene.String()
        red_team = graphene.ID(required=True)
        blue_team = graphene.ID(required=True)
        match_day = graphene.ID()
        tournament_id = graphene.ID()
        match_ended = graphene.Boolean()

    ok = graphene.Boolean()
    match = graphene.Field(Match)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        matchService = TournamentService()
        match = matchService.createMatch(input=input)
        return CreateMatch(match=match, ok=bool(match.id))


class CreateTournament(graphene.ClientIDMutation):
    """ Creazione di un torneo.
    """

    class Input:
        name = graphene.String()

    ok = graphene.Boolean()
    tournament = graphene.Field(Tournament)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        matchService = TournamentService()
        tournament = matchService.createTournament(input=input)
        return CreateTournament(tournament=tournament, ok=bool(tournament.id))


class UpdateTournament(graphene.ClientIDMutation):
    """ Mutation for updating a Tournament infos.
    """

    class Input:
        tournament_id = graphene.ID(required=True)
        name = graphene.String()

    ok = graphene.Boolean()
    tournament = graphene.Field(Tournament)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        matchService = TournamentService()
        updatedtournament = matchService.update_tournament(input)
        return UpdateTournament(
            tournament=updatedtournament,
            ok=bool(updatedtournament.id)
        )


class DeleteTournament(graphene.ClientIDMutation):
    """ Mutation for deleting a Tournament
    """

    class Input:
        tournament_id = graphene.ID(required=True)

    ok = graphene.Boolean()

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        matchService = TournamentService()
        object_deleted = matchService.delete_tournament(input)
        return DeleteTournament(ok=True if (object_deleted[0] == 1) else False)
