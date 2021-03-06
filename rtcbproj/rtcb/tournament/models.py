# -*- coding: utf-8 -*-
from django.db import models
from rtcb.team.models import Team


class Tournament(models.Model):
    name = models.CharField(
        verbose_name="Tournament name",
        max_length=50,
    )

    def __str__(self):
        return self.name


class Round(models.Model):
    """ Giornata del torneo
    """

    title = models.CharField(
        max_length=50,
        null=True,
        blank=True,
    )

    counter = models.PositiveIntegerField(
        default=0
    )

    tournament = models.ForeignKey(
        Tournament,
        related_name='tournament',
        null=True,
        on_delete=models.CASCADE,
    )


class MatchScore(models.Model):

    team = models.ForeignKey(
        Team,
        null=True,
        on_delete=models.SET_NULL,
        related_name="team_id",
    )
    score = models.PositiveIntegerField(
        default=0
    )
    color = models.CharField(
        max_length=4,
        null=True,
        blank=True,
    )


class Match(models.Model):
    class Meta:
        verbose_name = "match"
        verbose_name_plural = "matches"

    location = models.CharField(
        max_length=50,
        null=True,
        default="Sala Relax",
        verbose_name="Location",
        blank=True,
    )

    red_score = models.ForeignKey(
        MatchScore,
        related_name="red_score",
        null=True,
        on_delete=models.CASCADE
    )

    blue_score = models.ForeignKey(
        MatchScore,
        related_name="blue_score",
        null=True,
        on_delete=models.CASCADE
    )

    match_day = models.ForeignKey(
        Round,
        related_name='match_day',
        on_delete=models.CASCADE,
        null=True,
    )

    tournament_id = models.ForeignKey(
        Tournament,
        null=True,
        on_delete=models.CASCADE,
        related_name="tournament_id",
    )

    match_ended = models.BooleanField(
        default=False,
        verbose_name="Is the match ended?",
    )

    def __str__(self):
        return "Match: {} VS. {}".format(
            self.team_a.team_name,
            self.team_b.team_name,
            self.match_day,
        )
